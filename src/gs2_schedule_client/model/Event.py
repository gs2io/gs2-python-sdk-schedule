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


class Event(object):

    def __init__(self, params=None):
        if params is None:
            self.__name = None
            self.__meta = None
            self.__begin = None
            self.__end = None
        else:
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_meta(params['meta'] if 'meta' in params.keys() else None)
            self.set_begin(params['begin'] if 'begin' in params.keys() else None)
            self.set_end(params['end'] if 'end' in params.keys() else None)

    def get_name(self):
        """
        イベント名を取得
        :return: イベント名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        イベント名を設定
        :param name: イベント名
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

    def get_begin(self):
        """
        開始日時を取得
        :return: 開始日時
        :rtype: int
        """
        return self.__begin

    def set_begin(self, begin):
        """
        開始日時を設定
        :param begin: 開始日時
        :type begin: int
        """
        self.__begin = begin

    def get_end(self):
        """
        終了日時を取得
        :return: 終了日時
        :rtype: int
        """
        return self.__end

    def set_end(self, end):
        """
        終了日時を設定
        :param end: 終了日時
        :type end: int
        """
        self.__end = end

    def to_dict(self):
        return {
            "name": self.__name,
            "meta": self.__meta,
            "begin": self.__begin,
            "end": self.__end,
        }
