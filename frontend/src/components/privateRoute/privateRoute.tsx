import { Route, Redirect, RouteProps } from "react-router";

import { authStore } from "@pages/auth/auth.store";
import { AppRoute } from "@common/enums/app-route.enum";

export interface ProtectedRouteProps extends RouteProps {
  isAuthenticated: boolean;
  authenticationPath: string;
}

export class PrivateRoute extends Route<ProtectedRouteProps>{
  public render(){
    let redirectPath: string = "";
    if (!authStore.isSignedUp) {
      redirectPath = AppRoute.SIGNUP;
    }
    else if (!authStore.isLoggedIn){
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
