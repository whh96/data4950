#!/usr/bin/env python

"""Tests for `data4950_project` package."""


import unittest
from click.testing import CliRunner

from data4950_project import data4950_project
from data4950_project import cli


class TestData4950_project(unittest.TestCase):
    """Tests for `data4950_project` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'data4950_project.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
