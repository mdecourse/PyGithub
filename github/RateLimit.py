# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

from deprecated import deprecated

import github.GithubObject
import github.Rate


class RateLimit(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents RateLimits. The reference can be found here http://developer.github.com/v3/rate_limit
    """

    def __repr__(self):
        return self.get__repr__({"core": self._core.value})

    @property
    @deprecated(
        reason="""
            The rate object is deprecated. If you're writing new API client code
            or updating existing code, you should use the core object instead of
            the rate object. The core object contains the same information that
            is present in the rate object.
        """
    )
    def rate(self):  # pragma: no cover
        """
        (Deprecated) Rate limit for non-search-related API, use `core` instead

        :type: class:`github.Rate.Rate`
        """
        return self._core.value

    @property
    def core(self):
        """
        Rate limit for the non-search-related API

        :type: class:`github.Rate.Rate`
        """
        return self._core.value

    @property
    def search(self):
        """
        Rate limit for the Search API.

        :type: class:`github.Rate.Rate`
        """
        return self._search.value

    @property
    def graphql(self):
        """
        (Experimental) Rate limit for GraphQL API, use with caution.

        :type: class:`github.Rate.Rate`
        """
        return self._graphql.value

    def _initAttributes(self):
        self._core = github.GithubObject.NotSet
        self._search = github.GithubObject.NotSet
        self._graphql = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "core" in attributes:  # pragma no branch
            self._core = self._makeClassAttribute(github.Rate.Rate, attributes["core"])
        if "search" in attributes:  # pragma no branch
            self._search = self._makeClassAttribute(
                github.Rate.Rate, attributes["search"]
            )
        if "graphql" in attributes:  # pragma no branch
            self._graphql = self._makeClassAttribute(
                github.Rate.Rate, attributes["graphql"]
            )
