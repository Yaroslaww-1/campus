import { makeAutoObservable } from "mobx";

import api from "@api/api.helper";

interface AuthData {
  grant_type : string,
  client_id : string,
  client_secret : string,
  username : string,
  password : string,
}

export class AuthStore {
  isLoggedIn = false;
  token = "";
  constructor() {
    const token = localStorage.getItem("accessToken");
    if (token) this.token = token;
    makeAutoObservable(this);
    if (this.token && this.token.length > 0) {
      this.isLoggedIn = true;
    }
  }

  login(){
  }

  async setToken(values : string){
    const endpoint = "/api/users/connect/token";
    const formData = JSON.parse(values);
    const authData = {
      grant_type : "password",
      client_id : "ro.client",
      client_secret : "secret",
      username : "student@gmail.com", //formData.email,
      password : "studentPass", //formData.password,
    };
    this.token = JSON.stringify(await api.put<AuthData>(endpoint,  authData));
    localStorage.setItem("accessToken", this.token);
  }

  getToken(){
    this.token = localStorage.get("accessToken");
    return this.token;
  }

  async signUp(values : string) {
    await this.setToken(values);
    return this.token;
  }

  logout() {
    localStorage.removeItem("accessToken");
  }
}

export const authStore = new AuthStore();
