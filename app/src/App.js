import React from 'react';
import './App.css';
import axios from 'axios';
import ShowResultMessage from './showResultMessage';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      file: null,
      predictedVal: null,
      predictedLabel: null,
      showResultMessage: false
    };
  }

  handleSubmit = (e) => {
    const data = new FormData()
    data.append('file', this.state.file)
    axios.post('http://10.8.12.228:8080/upload/',data, {})
    .then(res => {
      if(res.status === 200){
        this.setState({
          predictedVal: res.data.value,
          predictedLabel: res.data.label,
          showResultMessage: true
        })
      }
    })
    e.preventDefault()
  }

  handleChange = (e) => {
    this.setState({
      file: e.target.files[0]
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
            this.state.showResultMessage && <ShowResultMessage label={this.state.predictedLabel} val={this.state.predictedVal} />
          }
        </body>
      </div>
    );
  }
}

export default App;
