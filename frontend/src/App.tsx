import { Route, Switch } from "react-router-dom";
import { AppRoute } from "./enums/app-route.enum";
import { HomePage } from "./pages";

export const App = () => {
  return (
    <Switch>
      <Route exact path={AppRoute.HOME} component={HomePage} />
    </Switch>
  );
};
