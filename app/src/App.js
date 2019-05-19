import React from 'react';
import './App.css';
import axios from 'axios';
import ShowResultMessage from './showResultMessage';
import { ClipLoader } from 'react-spinners';
const URL = 'http://localhost:8000/upload/'

const spinner = <ClipLoader sizeUnit={"px"} size={150} color={'white'} loading={this.state.loading} />

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      file: null,
      predictedVal: null,
      predictedLabel: null,
      showResultMessage: false,
      loading: false
    };
  }

  handleSubmit = (e) => {
    this.setState({
      loading: true
    })
    const data = new FormData()
    data.append('file', this.state.file)
    axios.post(URL ,data, {})
    .then(res => {
      if(res.status === 200){
        this.setState({
          predictedVal: res.data.value,
          predictedLabel: res.data.label,
          showResultMessage: true,
          loading: false
        })
      }
    })
    e.preventDefault()
  }

  handleChange = (e) => {
    this.setState({
      file: e.target.files[0],
      showResultMessage: false
    })
  }

  render() {
    return (
      <div className="App" onSubmit={this.handleSubmit}>
        <header className="App-header">
          <form>
            <input type='file' name='myFile' onChange={this.handleChange}/>
            <br />
            <input type='submit' />
          </form>
        </header>
        <body className="App-body">
          {
            this.state.loading? spinner : this.state.showResultMessage && <ShowResultMessage label={this.state.predictedLabel} val={this.state.predictedVal} />
          }
        </body>
      </div>
    );
  }
}

export default App;
