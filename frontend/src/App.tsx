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

import { PrivateRoute, ProtectedRouteProps } from "@components/privateRoute/privateRoute";
import { authStore } from "@pages/auth/auth.store";

const defaultProtectedRouteProps: ProtectedRouteProps = {
  isAuthenticated: authStore.isLoggedIn,
  authenticationPath: AppRoute.LOGIN,
};

export const App = () => {
  return (
    <>
      <Header></Header>
      <Switch>
        <Route exact path={AppRoute.HOME} component={HomePage} />
        <PrivateRoute {...defaultProtectedRouteProps} path={AppRoute.POSTS} component={PostsPage} />
        <PrivateRoute {...defaultProtectedRouteProps} path={AppRoute.USERS} component={UsersPage} />
        <PrivateRoute {...defaultProtectedRouteProps} path={AppRoute.USER} component={UserProfilePage} />
        <PrivateRoute {...defaultProtectedRouteProps} path={AppRoute.SCHEDULE} component={SchedulePage} />
        <PrivateRoute {...defaultProtectedRouteProps} path={AppRoute.COURSES} />
        <PrivateRoute {...defaultProtectedRouteProps} path={AppRoute.UPDATEUSERAVATAR} component={UpdateUserAvatar} />
        <Route path={[AppRoute.LOGIN, AppRoute.SIGNUP]} component={Auth} />
      </Switch>
    </>
  );
};
