import { Route, Switch } from "react-router-dom";

import { AppRoute } from "@common/enums/app-route.enum";

import { HomePage, PostsPage, UsersPage, SchedulePage } from "./pages";

export const App = () => {
  return (
    <Switch>
      <Route exact path={AppRoute.HOME} component={HomePage} />
      <Route path={AppRoute.POSTS} component={PostsPage} />
      <Route path={AppRoute.SCHEDULE} component={SchedulePage} />
      <Route path={AppRoute.USERS} component={UsersPage} />
    </Switch>
  );
};
