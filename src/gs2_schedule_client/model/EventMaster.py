# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

class EventMaster(object):

    def __init__(self, params=None):
        if params is None:
            self.__event_master_id = None
            self.__name = None
            self.__meta = None
            self.__type = None
            self.__absolute_begin = None
            self.__absolute_end = None
            self.__relative_trigger_name = None
            self.__relative_span = None
            self.__create_at = None
            self.__update_at = None
        else:
            self.set_event_master_id(params['eventMasterId'] if 'eventMasterId' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_meta(params['meta'] if 'meta' in params.keys() else None)
            self.set_type(params['type'] if 'type' in params.keys() else None)
            self.set_absolute_begin(params['absoluteBegin'] if 'absoluteBegin' in params.keys() else None)
            self.set_absolute_end(params['absoluteEnd'] if 'absoluteEnd' in params.keys() else None)
            self.set_relative_trigger_name(params['relativeTriggerName'] if 'relativeTriggerName' in params.keys() else None)
            self.set_relative_span(params['relativeSpan'] if 'relativeSpan' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)


    def get_event_master_id(self):
        """
        イベントマスターGRNを取得
        :return: イベントマスターGRN
        :rtype: unicode
        """
        return self.__event_master_id

    def set_event_master_id(self, event_master_id):
        """
        イベントマスターGRNを設定
        :param event_master_id: イベントマスターGRN
        :type event_master_id: unicode
        """
        self.__event_master_id = event_master_id

    def get_name(self):
        """
        イベントマスター名を取得
        :return: イベントマスター名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        イベントマスター名を設定
        :param name: イベントマスター名
        :type name: unicode
        """
        self.__name = name

    def get_meta(self):
        """
        メタデータを取得
        :return: メタデータ
        :rtype: unicode
        """
        return self.__meta

    def set_meta(self, meta):
        """
        メタデータを設定
        :param meta: メタデータ
        :type meta: unicode
        """
        self.__meta = meta

    def get_type(self):
        """
        期間を取得
        :return: 期間
        :rtype: unicode
        """
        return self.__type

    def set_type(self, type):
        """
        期間を設定
        :param type: 期間
        :type type: unicode
        """
        self.__type = type

    def get_absolute_begin(self):
        """
        絶対時間を選択した場合の開始日時を取得
        :return: 絶対時間を選択した場合の開始日時
        :rtype: int
        """
        return self.__absolute_begin

    def set_absolute_begin(self, absolute_begin):
        """
        絶対時間を選択した場合の開始日時を設定
        :param absolute_begin: 絶対時間を選択した場合の開始日時
        :type absolute_begin: int
        """
        self.__absolute_begin = absolute_begin

    def get_absolute_end(self):
        """
        絶対時間を選択した場合の終了日時を取得
        :return: 絶対時間を選択した場合の終了日時
        :rtype: int
        """
        return self.__absolute_end

    def set_absolute_end(self, absolute_end):
        """
        絶対時間を選択した場合の終了日時を設定
        :param absolute_end: 絶対時間を選択した場合の終了日時
        :type absolute_end: int
        """
        self.__absolute_end = absolute_end

    def get_relative_trigger_name(self):
        """
        相対時間を選択した場合の開始トリガー名を取得
        :return: 相対時間を選択した場合の開始トリガー名
        :rtype: unicode
        """
        return self.__relative_trigger_name

    def set_relative_trigger_name(self, relative_trigger_name):
        """
        相対時間を選択した場合の開始トリガー名を設定
        :param relative_trigger_name: 相対時間を選択した場合の開始トリガー名
        :type relative_trigger_name: unicode
        """
        self.__relative_trigger_name = relative_trigger_name

    def get_relative_span(self):
        """
        相対時間を選択した場合のトリガーを引いてからのイベント期間(分)を取得
        :return: 相対時間を選択した場合のトリガーを引いてからのイベント期間(分)
        :rtype: int
        """
        return self.__relative_span

    def set_relative_span(self, relative_span):
        """
        相対時間を選択した場合のトリガーを引いてからのイベント期間(分)を設定
        :param relative_span: 相対時間を選択した場合のトリガーを引いてからのイベント期間(分)
        :type relative_span: int
        """
        self.__relative_span = relative_span

    def get_create_at(self):
        """
        作成日時(エポック秒)を取得
        :return: 作成日時(エポック秒)
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        作成日時(エポック秒)を設定
        :param create_at: 作成日時(エポック秒)
        :type create_at: int
        """
        self.__create_at = create_at

    def get_update_at(self):
        """
        最終更新日時(エポック秒)を取得
        :return: 最終更新日時(エポック秒)
        :rtype: int
        """
        return self.__update_at

    def set_update_at(self, update_at):
        """
        最終更新日時(エポック秒)を設定
        :param update_at: 最終更新日時(エポック秒)
        :type update_at: int
        """
        self.__update_at = update_at

    def to_dict(self):
        return { 
            "eventMasterId": self.__event_master_id,
            "name": self.__name,
            "meta": self.__meta,
            "type": self.__type,
            "absoluteBegin": self.__absolute_begin,
            "absoluteEnd": self.__absolute_end,
            "relativeTriggerName": self.__relative_trigger_name,
            "relativeSpan": self.__relative_span,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
        }