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
import { CreatePost } from "@pages/posts/components/create-post";

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
        <Route path={AppRoute.UPDATE_USER_AVATAR} component={UpdateUserAvatar} />
        <Route path={[AppRoute.LOGIN, AppRoute.SIGNUP]} component={Auth} />
        <Route path={AppRoute.CREATE_POST} component={CreatePost} />
      </Switch>
    </>
  );
};
