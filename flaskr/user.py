"""
Program Name: user
By: Omer Alon
Date: 02/04/17
Program Version: 1.0.0
"""
import yaml
import information_server
import datetime
from teams_data import *
from global_constants import *


class User(object):

    USERS_DATA = "database/users.yaml"

    def __init__(self, username, password):
        """Set the class's attributes."""
        self.__username = username
        self.__password = password
        self.__teams = []
        self.__user_matches = []
        self.__information_source = information_server.InformationSource()

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def set_teams(self, picked_teams):
        """Set the teams' attribute and update the users file.


        Receives:
            picked_teams - A list that contains the teams
            that the user chose to follow on.
        """
        self.__teams = picked_teams
        with open(self.USERS_DATA, "a") as users_data:
            yaml.dump([{(self.__username, self.__password): picked_teams}],
                      users_data, default_flow_style=False)

    def locate_username(self):
        """Find the current user in the database by his username


        Returns:
            user - A dictionary that contains the
            username and password of the user (key) and
            the user's followed teams (value)
        """
        with open(self.USERS_DATA, "r") as users_file:
            users = yaml.load(users_file)
            if users:
                for user in users:
                    if self.__username == user.keys()[0][0]:
                        return user

    def check_details(self):
        """Check if the username or password already exists in one of the saves.


        Returns:
            A bool that indicates if the username/password exist or not.
        """
        if self.locate_username() or self.locate_password():
            return True
        return False

    def match_password(self):
        """Check if the user is exist int the database,
           meaning that the username is matching the password


        Returns:
            A bool that indicates if the username match the password
        """
        user = self.locate_username()
        if user:
            if self.__password == user.keys()[0][1]:
                return True
        return False

    def locate_password(self):
        """Find the current user in the database by his password


        Returns:
            user - A dictionary that contains the
            username and password of the user (key) and
            the user's followed teams (value)
        """
        with open(self.USERS_DATA, "r") as users_file:
            users = yaml.load(users_file)
            if users:
                for user in users:
                    if self.__password == user.keys()[0][1]:
                        return user

    def load_teams(self):
        """Restore the user's team to the teams' attribute."""
        user = self.locate_username()
        for value in user.values():
            for team in value:
                self.__teams.append(team)

    def get_changes_categorized(self):
        """Get all the changes that found.


        Returns:
            A lists of new matches, ended matches, goals, live matches
        """
        # get the changes from the information source
        new_matches, ended_matches, goals = \
            self.__information_source.get_changes()
        return self.get_user_matches(new_matches), \
            self.get_user_matches(ended_matches), \
            self.get_user_matches(goals), \
            self.__information_source.last_scores

    def get_user_matches(self, matches):
        """Check if the user's teams are on the given matches updates that was found.


        Receives:
            matches - A list of dictionaries that contains matches.

        Returns:
            A list of dictionaries that contains
            only the matches that belong to the user's teams.
        """
        return [match for match in matches if match[HOME] in self.__teams or
                match[AWAY] in self.__teams]

    def get_all_matches(self):
        """Get all the user matches(finished, live and future) together.


        Returns:
            A list that contains all the matches that belong to the user.
        """
        return self.__information_source.get_matches(self.__teams)

    def get_matches_categorized(self):
        """Get the finished, live and future matches categorized.


        Returns:
            A lists of finished matches, live matches, future matches.
        """
        live = self.__information_source.get_live_matches()
        return self.get_finished_matches(live), self.get_user_matches(live), \
            self.get_future_matches(live)

    def get_finished_matches(self, live):
        """Get only the finished matches.


        Receives:
            live - A string that contains the live matches.

        Returns:
            A list that contains the user teams' finished matches.
        """
        finished_matches = [match for match in self.get_all_matches() if
                            match[STATUS] == FINISHED]
        for i in xrange(len(finished_matches)):
            finished_matches[i] = User.choose_information(finished_matches[i])
        return User.check_in_live(finished_matches, live)

    def get_future_matches(self, live):
        """Get only the future matches.


        Receives:
            live - A string that contains the live matches.

        Returns:
            A list that contains the user teams' future matches.
        """
        future_matches = [match for match in self.get_all_matches() if
                          None in match[RESULT].values() and
                          match[STATUS] != POSTPONED]
        for i in xrange(len(future_matches)):
            future_matches[i] = User.choose_information(future_matches[i])
        return User.check_in_live(future_matches, live)

    @staticmethod
    def check_in_live(matches, live_matches):
        """Check special incidents.


        Receives:
            matches - A list of dictionaries that contains matches.
            live_matches - A list of dictionaries that contains live matches.

        Returns:
            matches - A list that contains
                      the given matches without the live matches.
        """
        for i in xrange(len(matches)):
            for live_match in live_matches:
                if matches[i][HOME] == live_match[HOME] \
                        and matches[i][DATE] == \
                        datetime.datetime.today().date():
                    matches.remove(matches[i])
        return matches

    @staticmethod
    def choose_information(match):
        """Edit the match values.


        Receives:
            match - A dictionary that contains finished/future match.

        Returns:
            edited_match - A list that contains
                           the given match without the Unnecessary values.
        """
        edited_match = {DATE: match[DATE],
                        HOME_GOALS: match[RESULT][HOME_GOALS],
                        AWAY_GOALS: match[RESULT][AWAY_GOALS]}
        try:
            edited_match[HOME] = TEAMS_DICT[match[HOME]]
        except KeyError:
            edited_match[HOME] = match[HOME]
        try:
            edited_match[AWAY] = TEAMS_DICT[match[AWAY]]
        except KeyError:
            edited_match[AWAY] = match[AWAY]
        return edited_match
