import { makeAutoObservable } from "mobx";
import QueryString from "qs";

import { AuthService } from "@api/services/auth.service";

export class AuthStore {
  isLoggedIn = false;
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
    try{
      await this.setToken(values);
      this.isLoggedIn = true;
      return this.token;
    }
    catch{
      this.isLoggedIn = false;
    }
  }

  async setToken(values : string){
    const formData = JSON.parse(values);
    const authData = QueryString.stringify({
      grant_type : "password",
      client_id : "ro.client",
      client_secret : "secret",
      username : formData.email,
      password : formData.password,
    });
    const token = await AuthService.getToken(authData);
    if (token) this.token = token;
  }

  async getToken(){
    const token = localStorage.getItem("accessToken");
    if (token) this.token = token;
    return this.token;
  }

  async signUp(values : string) {
    //TODO: add user to userslist
    try{
      await this.setToken(values);
      this.isLoggedIn = true;
      return this.token;
    }
    catch{
      this.isLoggedIn = false;
    }
  }

  logout() {
    localStorage.removeItem("accessToken");
    this.isLoggedIn = false;
  }

  async isTokenValid() {
    return await AuthService.isValid();
  }

}

export const authStore = new AuthStore();
