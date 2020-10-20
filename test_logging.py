import logging
from logging.handlers import QueueHandler
from queue import SimpleQueue
from unittest import TestCase


class TestLogging(TestCase):
    def setUp(self) -> None:
        self.expected_log_message = 'expected log message'
        self.wrong_log_message = 'wrong log message'

        self.queue = SimpleQueue()
        self.queue_handler = QueueHandler(self.queue)

        self.parent_log_name = 'test_log_1'
        self.log = logging.getLogger(self.parent_log_name)

        self.log.setLevel(logging.INFO)
        self.log.handlers.append(self.queue_handler)

        self.child_log_name = self.parent_log_name + '.child'
        self.child_log = logging.getLogger(self.child_log_name)

        self.child_log.setLevel(logging.INFO)
        # specifically not setting a handler to test propagation

        self.verbose_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)-10s  %(message)s')

    def test_queue_log_handler(self):
        self.log.info(self.expected_log_message)
        self.log.info(self.wrong_log_message)

        log_record: logging.LogRecord = self.queue.get()
        self.assertTrue(log_record.msg)
        self.assertEqual(self.expected_log_message, log_record.msg)
        self.assertNotEqual(self.wrong_log_message, log_record.msg)

    def test_hierarchical_name(self):
        self.child_log.info(self.expected_log_message)

        log_record: logging.LogRecord = self.queue.get()
        self.assertEqual(self.expected_log_message, log_record.msg)

        self.assertEqual(self.child_log_name, log_record.name)
        self.assertTrue(log_record.name.startswith(self.parent_log_name))
        self.assertTrue(log_record.name.endswith('child'))

    def test_propagate_false(self):
        self.child_log.info(self.expected_log_message)
        self.child_log.propagate = False
        self.child_log.info(self.wrong_log_message)

        self.assertEqual(1, self.queue.qsize())
        log_record = self.queue.get()
        self.assertEqual(self.expected_log_message, log_record.msg)
        self.assertTrue(self.queue.empty())
        self.assertNotEqual(self.wrong_log_message, log_record.msg)

        self.child_log.propagate = True
        self.child_log.info('one')
        self.child_log.info('two')

        self.assertEqual(2, self.queue.qsize())

    def test_default_log_name(self):
        root_logger = logging.getLogger()
        self.assertEqual('root', root_logger.name)

    def test_formatter(self):
        self.log.info(self.expected_log_message)
        actual_before = self.queue.get().msg

        self.assertEqual(self.expected_log_message, actual_before)

        self.queue_handler.setFormatter(self.verbose_formatter)
        self.log.info(self.expected_log_message)

        actual_after = self.queue.get().msg
        self.assertTrue(actual_after.endswith(self.expected_log_message))
        self.assertFalse(actual_after.startswith(self.expected_log_message))

        self.assertIn(self.parent_log_name, actual_after)
        self.assertIn(logging.getLevelName(logging.INFO), actual_after)

        self.assertNotEqual(self.expected_log_message, actual_after)

    def test_root_name(self):
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.INFO)

        self.queue_handler.setFormatter(self.verbose_formatter)
        root_logger.handlers.append(self.queue_handler)

        root_logger.info(self.expected_log_message)

        actual = self.queue.get().msg

        self.assertIn(root_logger.name, actual, 'expecting "root" in log message')
        self.assertNotIn(self.parent_log_name, actual, 'not expecting "test_log_1" in log message')
        self.assertIn(logging.getLevelName(root_logger.level), actual, 'expecting "INFO" in log message')
        self.assertNotIn(__name__, actual, 'not module class name in log message')

    def test_log_levels(self):
        self.assertEqual(logging.INFO, self.log.level)

        should_not_show_up = 'should not show up'
        self.log.debug(should_not_show_up)

        self.assertTrue(self.queue.empty(), 'info log level should ignore debug log message')

    def test_change_level(self):
        self.assertEqual(logging.INFO, self.log.level)

        should_not_show_up = 'should not show up'
        self.log.debug(should_not_show_up)

        self.assertTrue(self.queue.empty(), 'info log level should ignore debug log message')

        self.log.setLevel(logging.DEBUG)
        should_show_up = 'should show up'
        self.log.debug(should_show_up)

        self.assertFalse(self.queue.empty())
        acutal_log_record = self.queue.get()
        self.assertEqual(should_show_up, acutal_log_record.message)
