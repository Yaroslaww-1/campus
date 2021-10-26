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
  isSignedUp = false;
  token = "";
  constructor() {
    this.getToken();
    makeAutoObservable(this);
    if (this.token && this.token.length > 0) {
      this.isLoggedIn = true;
      this.isSignedUp = true;
    }
  }

  async login(values : string){
    await this.setToken(values)
      .then( ()  => {this.isLoggedIn = true;})
      .catch(err => {this.isSignedUp = false; this.isLoggedIn = false;});
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
    await api.put<AuthData>(endpoint,  authData)
      .then( token  => {this.token = JSON.stringify(token); localStorage.setItem("accessToken", this.token);})
      .catch(err => {this.isLoggedIn = false;});
  }

  getToken(){
    const token = localStorage.getItem("accessToken");
    if (token) this.token = token;
    return this.token;
  }

  async signUp(values : string) {
    await this.setToken(values)
      .then( ()  => {this.isSignedUp = true; this.isLoggedIn = true;})
      .catch(err => {this.isSignedUp = false; this.isLoggedIn = false;});
    return this.token;
  }

  logout() {
    localStorage.removeItem("accessToken");
    this.isLoggedIn = false;
  }
}

export const authStore = new AuthStore();
