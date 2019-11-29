from .context import bitbored

from bitbored import migrate
import pytest
import os


def test_migrate():
    m = migrate.Migrate(os.getcwd() + '/tests/resources/bit-test.txt')
    bits = m.migrate()
    assert len(bits) == 1
    assert len(bits[0]) == 3

def test_migrate_bits():
    m = migrate.Migrate(os.getcwd() + '/tests/resources/bits-test.txt')
    bits = m.migrate()
    assert len(bits) == 2
    assert len(bits[0]) == 3
    assert len(bits[1]) == 4
