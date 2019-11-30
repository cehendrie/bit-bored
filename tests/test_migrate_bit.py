from .context import bitbored

from bitbored import migrate_bit
import pytest


class TestMigrateBit(object):
    def test_to_json(self):
        mb = migrate_bit.MigrateBit(['Character: Says something.'])
        json = mb.to_json()
        assert len(json) == 1
        assert 'bit' in json
        assert len(json['bit']) == 1
        assert json['bit'][0] == 'Character: Says something.'

    def test_to_json_multi_bit(self):
        mb = migrate_bit.MigrateBit(
            [
                'Character 1: Says something.',
                'Character 2: Says something else.'
            ])
        json = mb.to_json()
        assert len(json) == 1
        assert 'bit' in json
        assert len(json['bit']) == 2
        assert json['bit'][0] == 'Character 1: Says something.'
        assert json['bit'][1] == 'Character 2: Says something else.'

    def test_to_json_all_fields(self):
        mb = migrate_bit.MigrateBit(
            [
                '<scenerio>',
                'Character: Says something.',
                '- comment'
            ])
        json = mb.to_json()
        assert len(json) == 3
        assert 'scenerio' in json
        assert json['scenerio'] == '<scenerio>'
        assert 'bit' in json
        assert len(json['bit']) == 1
        assert json['bit'][0] == 'Character: Says something.'
        assert 'comments' in json
        assert len(json['comments']) == 1
        assert json['comments'][0] == '- comment'

    def test_to_json_multiple_comments(self):
        mb = migrate_bit.MigrateBit(
            [
                'Character: Says something.',
                '- comment 1',
                '- comment 2'
            ])
        json = mb.to_json()
        assert len(json) == 2
        assert 'bit' in json
        assert len(json['bit']) == 1
        assert json['bit'][0] == 'Character: Says something.'
        assert 'comments' in json
        assert len(json['comments']) == 2
        assert json['comments'][0] == '- comment 1'
        assert json['comments'][1] == '- comment 2'

    def test__is_valid(self):
        mb = migrate_bit.MigrateBit(['bit'])
        is_valid = mb._is_valid({'bit': ['Character: Says something.']})
        assert is_valid == True

    def test__is_valid_empty_json(self):
        mb = migrate_bit.MigrateBit(['bit'])
        is_valid = mb._is_valid({'scenerio': 'scenerio'})
        assert is_valid == False

    def test__is_valid_no_bit(self):
        mb = migrate_bit.MigrateBit(['bit'])
        is_valid = mb._is_valid({})
        assert is_valid == False
