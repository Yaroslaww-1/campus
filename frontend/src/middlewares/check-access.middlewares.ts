import { NavigationGuardNext, RouteLocationNormalized } from "vue-router";

import { AppRoute } from "@common/enums/app-route.enum";

const checkAccessMiddleware = async (
  to: RouteLocationNormalized,
  from: RouteLocationNormalized,
  next: NavigationGuardNext,
): Promise<void> => {
  const currentUserId = localStorage.get("accessToken");
  const isAuthRoute = to.matched.some(item => item.meta?.isAuth);

  if (isAuthRoute && currentUserId) {
    next();
    return;
  }
  if (isAuthRoute) {
    next({ path: AppRoute.LOGIN });
    return;
  }

  next();
};

export { checkAccessMiddleware };