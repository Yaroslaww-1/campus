import { Route, Switch } from "react-router-dom";

import { AppRoute } from "@common/enums/app-route.enum";

import { HomePage, PostsPage, Auth } from "./pages";

export const App = () => {
  return (
    <div className="wrapper">
      <Switch>
        <Route path={[AppRoute.LOGIN, AppRoute.SIGNUP]} component={Auth}/>
        <Route exact path={AppRoute.HOME} component={HomePage} />
        <Route path={AppRoute.POSTS} component={PostsPage} />
      </Switch>
    </div>
  );
};
