import QueryString from "qs";

import api, { apiWithAuth } from "../api.helper";

export class AuthService {
  static async getToken(authData:string): Promise<string|void> {
    const endpoint = "/users/connect/token";
    try{
      const token = await api.post<string, string>(endpoint, authData, "application/x-www-form-urlencoded");
      const tokenParse = QueryString.parse(token).access_token;
      let tokenString = "";
      if (tokenParse){
        tokenString = tokenParse?.toString();
        localStorage.setItem("accessToken", tokenString);
      }
      return tokenString;
    }
    catch (err){
      alert(JSON.stringify("Try again later", null, 2));
    }
  }

  static async isValid(): Promise<boolean> {
    const endpoint = "/users/authenticatedUser";
    try{
      await apiWithAuth.get<string, string>(endpoint);
      return true;
    }
    catch{
      return false;
    }
  }
}