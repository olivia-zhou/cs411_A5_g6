import { useState } from 'react'
import axios from "axios";
import './App.css';
import React from 'react';
import Map from "./Map";

import { SpotifyAuth, Scopes } from 'react-spotify-auth'
import 'react-spotify-auth/dist/index.css' // if using the included styles

import Cookies from 'js-cookie';

function App() {

  // Give App() a state to store login, etc. information

  class WeatherForm extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        latitude: 42.3497644,
        longitude: -71.1041491,
        isSubmitted: false,
        subTime: '',
        subForecast: ''
      };
  
      this.handleInputChange = this.handleInputChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
    }
  
    handleInputChange(event) {
      const target = event.target;
      const value = target.value;
      const name = target.name;
  
      this.setState({
        [name]: value
      });
    }
  
    handleSubmit(event) {
      this.setState({isSubmitted: true})
    
      axios({
        method: "GET",
        baseURL:"http://localhost:5000",
        url:"/weather?lat=" + this.state.latitude + "&lon=" + this.state.longitude,
      })
      .then((response) => {
        const res =response.data
        this.state.subTime = res.name
        this.state.subForecast = res.shortForecast
      }).catch((error) => {
        if (error.response) {
          console.log(error.response)
          console.log(error.response.status)
          console.log(error.response.headers)
          }
      });

      alert('The weather ' + this.state.subTime.toLowerCase() + ' will be ' + this.state.subForecast.toLowerCase());
      event.preventDefault();
      
    }
  
    render() {
      return (
        <div>
          <form onSubmit={this.handleSubmit}>
            <p>Enter the coordinates of the location whose weather you'd like to check: </p>
            <label>
              Longitude:
              <input
                name="longitude"
                type="number"
                value={this.state.longitude}
                onChange={this.handleInputChange} />
            </label>
            <br />
            <label>
              Latitude:
              <input
                name="latitude"
                type="number"
                value={this.state.latitude}
                onChange={this.handleInputChange} />
            </label>
            <input type="submit" value="Submit" />
          </form>
          <section>
              <Map />
          </section>
        </div>
        
      );
    }
  }

  class LogoutButton extends React.Component {
    constructor(props) {
      super(props);
      this.state = {};
      //this.handleClick = this.handleClick.bind(this);
    }

    handleClick(event)
    {
      axios({
        method: "GET",
        baseURL:"http://localhost:5000",
        url:"/logout",
      })
      .then((response) => {
        window.location = 'http://localhost:5000/logout'
      }).catch((error) => {
        if (error.response) {
          console.log(error.response)
          console.log(error.response.status)
          console.log(error.response.headers)
          }
      });
    }

    render() {
      return (
        <button onClick={this.handleClick}>Logout</button>
      )
    }
  }

  class LoginButton extends React.Component {
    constructor(props) {
      super(props);
      this.state = {};
    }

    handleLogin(event) // Can probably simplify this to just be "window.location = 'http://localhost:5000/login'"
    {
      {/* window.location.replace('https://accounts.spotify.com/en/authorize?response_type=code&client_id=409b58756fd146ec81debb62c51eb887&redirect_uri=http://127.0.0.1:5000/callback&scope=ugc-image-upload user-read-email user-read-private user-top-read playlist-modify-public playlist-modify-private playlist-read-private') */}
      axios({
        method: "GET",
        baseURL:"http://localhost:5000",
        url:"/login",
      })
      .then((response) => {
        const res = response.data
        if(response.data.redirect == '/'){
          window.location = ""
        } else if(response.data.redirect == '/login') {
          window.location = "/login"
        } else if(response.data.redirect == 'https://accounts.spotify.com/en/authorize?response_type=code&client_id=409b58756fd146ec81debb62c51eb887&redirect_uri=http://127.0.0.1:5000/callback&scope=ugc-image-upload user-read-email user-read-private user-top-read playlist-modify-public playlist-modify-private playlist-read-private'){
          window.location = "http://localhost:5000/login"
        } else {
          window.location = "http://localhost:5000/login"
        }
        alert(response.data);
      }).catch((error) => {
        if (error.response) {
          console.log(error.response)
          console.log(error.response.status)
          console.log(error.response.headers)
          }
      });
      alert('Login handled!');
    }

    render() {
      return (
        <button onClick={this.handleLogin}>Login</button>
      )
    }
  }

  class LogButton extends React.Component {

    constructor(props) {
      super(props);
      this.handleLoginClick = this.handleLoginClick.bind(this);
      this.handleLogoutClick = this.handleLogoutClick.bind(this);
      this.state = {isLoggedIn: false};
      // const [token, setToken] = React.useState(Cookies.get("spotifyAuthToken"))
    }
  
    handleLoginClick() {
      this.setState({isLoggedIn: true}); // Paste login class handleClick() here
    }
  
    handleLogoutClick() {
      this.setState({isLoggedIn: false}); // Paste logout class handleClick() here
      axios({
        method: "GET",
        baseURL:"http://localhost:5000",
        url:"/logout",
      })
      .then((response) => {
        window.location = 'http://localhost:5000/logout'
      }).catch((error) => {
        if (error.response) {
          console.log(error.response)
          console.log(error.response.status)
          console.log(error.response.headers)
          }
      });
      alert('Logout handled');
    }
  
    render() {
      const isLoggedIn = this.state.isLoggedIn;
      let button;
      if (isLoggedIn) {
        button = <button onClick={this.handleLogoutClick}>Logout</button>;
      } else {
        button = <SpotifyAuth
        redirectUri = 'http://127.0.0.1:5000/callback'
        clientID='409b58756fd146ec81debb62c51eb887'
        scopes={[Scopes.userReadPrivate, Scopes.userReadEmail]}
        onAccessToken = {(token) => setToken(token)}/>
      }
  
      return (
        <div>
          {button}
        </div>
      );
    }
  }

  class PlaylistButton extends React.Component {
    handleGenerate(){
      alert("WIP")
    }
    render() {
      return <button onClick={this.handleGenerate}>Generate playlist!</button>
    }
  }

  class OauthButton extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        args : window.location.pathname
      };
    }

    handleOauth(event) // Can probably simplify this to just be "window.location = 'http://localhost:5000/login'"
    {
      {/* window.location.replace('https://accounts.spotify.com/en/authorize?response_type=code&client_id=409b58756fd146ec81debb62c51eb887&redirect_uri=http://127.0.0.1:5000/callback&scope=ugc-image-upload user-read-email user-read-private user-top-read playlist-modify-public playlist-modify-private playlist-read-private') */}
      alert((window.location.hash).substring(1))
      axios({
        method: "GET",
        baseURL:"http://localhost:5000",
        url:"/generate_playlist?"+(window.location.hash).substring(1),
      })
      .then((response) => {
        const res = response.data
      }).catch((error) => {
        if (error.response) {
          console.log(error.response)
          console.log(error.response.status)
          console.log(error.response.headers)
          }
      });
    }

    render() {
      return (
        <button onClick={this.handleOauth}>Please God</button>
      )
    }
  }
   // new line start

  const wForm = <WeatherForm/>
  const loginForm = <LoginButton/>
  const logoutForm = <LogoutButton/>
  const [token, setToken] = React.useState(Cookies.get("spotifyAuthToken"))
  const logForm = <LogButton/>
  const playlistButton = <PlaylistButton/>
  const spotPls = <OauthButton/>

  return (
    <div className="App">
      <header className="App-header">
        {/* new line start*/}
        <h3>Day 111: All hope is fading and I haven't seen another person in weeks.</h3>
        <p>Final login/Logout button here:</p>{logForm}
        <section>
          <Map />
        </section>
        <SpotifyAuth
          // redirectUri = 'http://127.0.0.1:5000/callback'
          redirectUri = 'http://127.0.0.1:3000/'
          clientID='409b58756fd146ec81debb62c51eb887'
          scopes={[Scopes.userReadPrivate, Scopes.userReadEmail, Scopes.userTopRead, Scopes.playlistModifyPublic, Scopes.playlistModifyPrivate, Scopes.playlistReadPrivate, Scopes.ugcImageUpload]}
          onAccessToken = {(token) => setToken(token)}
        />
        {playlistButton}
        {logoutForm}
        {spotPls}
         {/* end of new line */}
      </header>
    </div>
  );
}

export default App;

