from .context import bitbored

from bitbored import migrate
import pytest
import os


def test_migrate():
    m = migrate.Migrate(os.getcwd() + '/tests/resources/bit-test.txt')
    bits = m.migrate()
    assert len(bits) == 1

def test_migrate_bits():
    m = migrate.Migrate(os.getcwd() + '/tests/resources/bits-test.txt')
    bits = m.migrate()
    assert len(bits) == 2
