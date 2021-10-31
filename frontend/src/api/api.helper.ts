import axios, { AxiosInstance, AxiosError } from "axios";

import { stringifyParams } from "../common/helpers/url.helper";

const BASE_URL = process.env.REACT_APP_API_URL || "/api";

class Api {
  instance: AxiosInstance;
  private readonly commonHeaders: {
    [key in string]: string;
  };
  constructor() {
    this.instance = axios.create({
      baseURL: BASE_URL,
      headers: {
        "Content-Type": "application/json",
      },
    });
    this.commonHeaders = { "Content-Type": "application/json" };
  }

  async get<Response = unknown, Params = unknown>(url: string, params?: Params): Promise<Response> {
    const response = await this.instance
      .get<Response>(`${url}?${stringifyParams(params)}`, {
        headers: this.commonHeaders,
        data: {},
      })
      .then(({ data }) => data)
      .catch(this.handleError);
    return this.validateAndReturnResponse<Response>(response);
  }

  async post<Response = unknown, Payload = unknown>(url: string, payload: Payload, contentType?: string ): Promise<Response> {
    const response = await this.instance
      .post(url, payload, contentType? {
        headers: { "Content-Type": contentType },
      }:{
        headers: this.commonHeaders,
      })
      .then(({ data }) => data)
      .catch(this.handleError);
    return this.validateAndReturnResponse<Response>(response);
  }

  async put<Response = unknown, Payload = unknown>(url: string, payload: Payload): Promise<Response> {
    const response = await this.instance
      .put(url, payload, {
        headers: this.commonHeaders,
      })
      .then(({ data }) => data)
      .catch(this.handleError);
    return this.validateAndReturnResponse<Response>(response);
  }

  async delete<Response = unknown, Payload = unknown>(url: string, data?: Payload): Promise<Response> {
    const response = await this.instance
      .delete(url, {
        headers: this.commonHeaders,
        data,
      })
      .then(({ data }) => data)
      .catch(this.handleError);
    return this.validateAndReturnResponse<Response>(response);
  }

  private validateAndReturnResponse<Response>(responseData: Response | void): Response {
    if (!responseData) {
      throw new Error();
    } else {
      return responseData;
    }
  }

  private handleError(error: AxiosError) {
    if (error.response) {
      // return { error: error.response.data };
      throw new Error(error.response.data.error);
    } else if (error.request) {
      // return { error: error.request.responseText };
      throw new Error(error.request.responseText);
    } else {
      // return { error: error.message };
      throw new Error(error.message);
    }
  }
}

class ApiWithAuth extends Api {
  constructor() {
    super();

    this.instance = axios.create({
      baseURL: BASE_URL,
      headers: {
        "Content-Type": "application/json",
      },
      withCredentials: true,
    });

    this.initInterceptor();
  }

  initInterceptor(): void {
    this.instance.interceptors.request.use(
      request => {
        request.headers.authorization = `Bearer ${localStorage.getItem("accessToken")}`;
      },
      error => {
        return Promise.reject(error);
      },
    );
  }
}

const api = new Api();
const apiWithAuth = new ApiWithAuth();

export { Api, ApiWithAuth };
export { api, apiWithAuth };

export default new Api();