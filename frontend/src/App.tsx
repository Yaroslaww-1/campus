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

import { authStore } from "@pages/auth/auth.store";

//add onEnter for private pages
function authRequired(nextState : unknown, replace: Function) {
  if (!authStore.isLoggedIn) {
    replace(AppRoute.SIGNUP);
  }
}

export const App = () => {
  return (
    <>
      <Header></Header>
      <Switch>
        <Route exact path={AppRoute.HOME} component={HomePage} />
        <Route path={AppRoute.POSTS} component={PostsPage} />
        <Route path={AppRoute.USERS} component={UsersPage} />
        <Route path={AppRoute.USER} component={UserProfilePage} />
        <Route path={AppRoute.SCHEDULE} component={SchedulePage} />
        <Route path={AppRoute.UPDATEUSERAVATAR} component={UpdateUserAvatar} />
        <Route path={[AppRoute.LOGIN, AppRoute.SIGNUP]} component={Auth} />
      </Switch>
    </>
  );
};
