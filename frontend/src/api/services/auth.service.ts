import QueryString from "qs";

import api, { apiWithAuth } from "../api.helper";

export class AuthService {
  static async getToken(authData:string): Promise<string|void> {
    const endpoint = "/users/connect/token";
    const token = await api.post<string, string>(endpoint, authData)
      .then( token  => {
        const token_parse = QueryString.parse(token).access_token;
        if (token_parse){
          token = token_parse?.toString();
          localStorage.setItem("accessToken", token);
        }
        return token;
      });
    return token;
  }

  static async isValid(): Promise<boolean> {
    const endpoint = "/users/authenticatedUser";
    let isValid = false;
    await apiWithAuth.get<string, string>(endpoint)
      .then(() => isValid = true)
      .catch(() => isValid = false);
    return isValid;
  }
}