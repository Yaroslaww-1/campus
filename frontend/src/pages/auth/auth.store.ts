import { makeAutoObservable } from "mobx";
import api from "@api/api.helper";

export class AuthStore {
  isLoggedIn = false;
  constructor() {
    const token = localStorage.get("accessToken");
    makeAutoObservable(this);
    if (token) {
      this.isLoggedIn = true;
    }
  }

  login(){

  }

  async signUp(values : string) {
    const endpoint = "singup";
    const token = await api.put<FormData>(endpoint, values);
    localStorage.setItem("accessToken", JSON.stringify(token));
    return token;
  }

  logout() {
    localStorage.removeItem("accessToken");
  }
}

export const authStore = new AuthStore();
