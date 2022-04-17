import { useState } from 'react'
import axios from "axios";
import './App.css';
import React from 'react'

function App() {

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
        </div>
        
      );
    }
  }

   // new line start
  const [profileData, setProfileData] = useState(null)
  const wForm = <WeatherForm/>

  function getData(lat, lon) {
    axios({
      method: "GET",
      baseURL:"http://localhost:5000",
      url:"/weather?lat="+lat+"&lon="+lon,
    })
    .then((response) => {
      const res =response.data
      setProfileData(({
        profile_name: res.name,
        about_me: res.shortForecast}))
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    })}
    //end of new line 

  return (
    <div className="App">
      <header className="App-header">
        {/* new line start*/}
        {wForm}
        {/* <p>To get the weather forecast: </p><button onClick={() => getData("42.3061","-71.0589")}>Click me</button>
        {profileData && <div>
              <p>The forecast for {profileData.profile_name}</p>
              <p>is {profileData.about_me}</p>
            </div>
        } */}
         {/* end of new line */}
      </header>
    </div>
  );
}

export default App;