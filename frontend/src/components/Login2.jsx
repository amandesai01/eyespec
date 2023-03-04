import { useState } from "react";
import sapiensImg from "./assets/sapiens.png";
import { useHistory } from "react-router-dom";
import Navbar from "./Navbar";

function Login2({ setUser }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const history = useHistory();

  function usernameHandler(event) {
    setUsername(event.target.value);
  }

  function passwordHandler(event) {
    setPassword(event.target.value);
  }

  function authenticateUser() {
    // if user is authenticated
    setUser({ username });
    history.push("/home");
  }

  return (
    <>
      <div class="hero min-h-screen bg-base-200">
        <div class="hero-content flex-col lg:flex-row">
          <div class="text-center lg:text-left">
            <h1 class="text-5xl font-bold">Login now!</h1>
            <p class="py-6">
              Extract Data from your PDF to an easily accessible understandable
              excel format
            </p>
          </div>
          <div class="card flex-shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
            <div class="card-body">
              <div class="form-control">
                <input
                  type="text"
                  placeholder="Username"
                  class="input input-bordered"
                  onChange={usernameHandler}
                />
              </div>
              <div class="form-control">
                <input
                  type="password"
                  placeholder="Password"
                  class="input input-bordered"
                  onChange={passwordHandler}
                />
              </div>
              <div class="form-control mt-6">
                <button class="btn btn-outline" onClick={authenticateUser}>
                  Login
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default Login2;
