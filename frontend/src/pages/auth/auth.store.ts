import { makeAutoObservable } from "mobx";
import QueryString from "qs";

import api, { apiWithAuth } from "@api/api.helper";
import { RouteProps } from "react-router";

interface AuthData {
  grant_type : string,
  client_id : string,
  client_secret : string,
  username : string,
  password : string,
}

export class AuthStore {
  isLoggedIn = false;
  isSignedUp = true;
  token = "";
  path = "/";
  constructor() {
    this.getToken();
    makeAutoObservable(this);
    if (this.token && this.token.length > 0) {
      this.isLoggedIn = true;
    }
  }

  async login(values : string){
    await this.setToken(values)
      .then( ()  => {this.isLoggedIn = true;})
      .catch(err => {this.isLoggedIn = false;});
  }

  async setToken(values : string){
    const endpoint = "/users/connect/token";
    const formData = JSON.parse(values);
    const authData = QueryString.stringify({
      grant_type : "password",
      client_id : "ro.client",
      client_secret : "secret",
      username : formData.email,
      password : formData.password,
    });
    await api.post<string, string>(endpoint, authData)
      .then( token  => {
        const token_parse = QueryString.parse(token).access_token;
        if (token_parse){
          this.token = token_parse?.toString();
          localStorage.setItem("accessToken", this.token);
        }
      })
      .catch(err => {this.isLoggedIn = false;});
  }

  async getToken(){
    const token = localStorage.getItem("accessToken");
    if (token) this.token = token;
    return this.token;
  }

  async signUp(values : string) {
    //TODO: add youser to userslist
    await this.setToken(values)
      .then( ()  => {this.isLoggedIn = true;})
      .catch(err => {this.isLoggedIn = false;});
    return this.token;
  }

  logout() {
    localStorage.removeItem("accessToken");
    this.isLoggedIn = false;
  }

  async isTokenValid() {
    const endpoint = "/users/authenticatedUser";
    let isValid = false;
    await apiWithAuth.get<string, string>(endpoint)
      .then(data => isValid = true)
      .catch(err => isValid = false);
    return isValid;
  }

}

export const authStore = new AuthStore();
