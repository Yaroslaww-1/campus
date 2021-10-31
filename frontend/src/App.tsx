import { Route, Switch } from "react-router-dom";

import { AppRoute } from "@common/enums/app-route.enum";

import { Header } from "@components/header";

import {
  HomePage,
  PostsPage,
  UsersPage,
  UserProfilePage,
  SchedulePage,
  UpdateUserAvatar,
  Auth,
} from "./pages";

import { PrivateRoute } from "@components/privateRoute/privateRoute";

export const App = () => {
  return (
    <>
      <Header></Header>
      <Switch>
        <Route exact path={AppRoute.HOME} component={HomePage} />
        <PrivateRoute path={AppRoute.POSTS} component={PostsPage} />
        <PrivateRoute path={AppRoute.USERS} component={UsersPage} />
        <PrivateRoute path={AppRoute.USER} component={UserProfilePage} />
        <PrivateRoute path={AppRoute.SCHEDULE} component={SchedulePage} />
        <PrivateRoute path={AppRoute.COURSES} />
        <PrivateRoute path={AppRoute.UPDATEUSERAVATAR} component={UpdateUserAvatar} />
        <Route path={[AppRoute.LOGIN, AppRoute.SIGNUP]} component={Auth} />
      </Switch>
    </>
  );
};
