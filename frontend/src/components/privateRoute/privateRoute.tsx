import { Route, Redirect, RouteProps } from "react-router";

import { authStore } from "@pages/auth/auth.store";
import { AppRoute } from "@common/enums/app-route.enum";

export interface ProtectedRouteProps extends RouteProps {
  isAuthenticated: boolean;
  authenticationPath: string;
}

export const defaultProtectedRouteProps: ProtectedRouteProps = {
  isAuthenticated: authStore.isLoggedIn,
  authenticationPath: AppRoute.LOGIN,
};

export class PrivateRoute extends Route<ProtectedRouteProps>{
  public render(){
    let redirectPath: string = "";
    authStore.path = this.props.path?.toString() || AppRoute.HOME;
    if (!authStore.isSignedUp) {
      redirectPath = AppRoute.SIGNUP;
    }
    else if (!authStore.isLoggedIn || !authStore.isTokenValid()){
      redirectPath = AppRoute.LOGIN;
    }
    if (redirectPath) {
      const renderComponent = () => (<Redirect to={ { pathname: redirectPath } }/>);
      return <Route {...this.props} component={renderComponent} render={undefined}/>;
    } else {
      return <Route {...this.props}/>;
    }
  }
}
