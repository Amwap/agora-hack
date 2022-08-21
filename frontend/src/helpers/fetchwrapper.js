import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL;

export const fetchWrapper = {
  get: request("GET"),
  post: request("POST"),
  put: request("PUT"),
  delete: request("DELETE"),
  download: download(),
};

function download() {
  return (url, filename, return_blob = false) => {
    const base_url = `${API_URL}${url}`;
    axios({
      url: base_url,
      method: "GET",
      headers: authHeader(base_url),
      responseType: "blob", // important
    }).then((response) => {
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", filename);
      document.body.appendChild(link);
      link.click();
    });
  };
}

function request(method) {
  return (url, body) => {
    const base_url = `${API_URL}${url}`;
    const requestOptions = {
      method,
      headers: authHeader(base_url),
    };
    if (body instanceof FormData) {
      requestOptions.body = body;
    } else if (body) {
      requestOptions.headers["Content-Type"] = "application/json";
      requestOptions.body = JSON.stringify(body);
    }

    return fetch(base_url, requestOptions).then(handleResponse);
  };
}

function authHeader(url) {
  // return auth header with jwt if user is logged in and request is to the api url
  return {};
}

function handleResponse(response) {
  return response.text().then((text) => {
    const data = text && JSON.parse(text);
    if (!response.ok) {
      const { access, logout } = useAuthStore();
      if ([401, 403].includes(response.status) && access) {
      } else if ([400].includes(response.status)) {
        errorCatcher.catch(data);
      }

      errorCatcher.catch(data);
      const error = (data && data.message) || response.statusText;
      return Promise.reject(error);
    }
    return data;
  });
}
