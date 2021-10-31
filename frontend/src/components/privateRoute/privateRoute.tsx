import { Route, Redirect, RouteProps } from "react-router";

import { authStore } from "@pages/auth/auth.store";
import { AppRoute } from "@common/enums/app-route.enum";

export const PrivateRoute: React.FC<RouteProps> = ({ path, component }) =>{
  let redirectPath: string = "";
  authStore.path = path?.toString() || AppRoute.HOME;
  if (!authStore.isLoggedIn || !authStore.isTokenValid()){
    redirectPath = AppRoute.LOGIN;
  }
  if (redirectPath) {
    const renderComponent = () => (<Redirect to={ { pathname: redirectPath } }/>);
    return <Route path={path} component={renderComponent} render={undefined}/>;
  } else {
    return <Route path={path} component={component}/>;
  }
};
