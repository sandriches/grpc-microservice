import React from 'react';
import axios from 'axios';
import './App.css';

class App extends React.Component {
    constructor() {
      super();
      this.state = { data: [] };
    }

    async componentDidMount() {
      const response = await axios(`http://localhost:5000`);
      this.setState({ data: response.data });
    }

    render() {
      return (
        <div className="App">
          <header className="App-header">
            <h1>Meter Usage Data</h1>
            <table className="table">
                <thead>
                    <tr>
                        <th>Time</th>
                        <th>Meter Usage</th>
                    </tr>
                </thead>
                <tbody>
                    {this.state.data.map((data) => {
                        return(
                            <tr>
                                <td>{data.time}</td>
                                <td>{data.meterusage}</td>
                            </tr>
                        )
                        })}
                </tbody>
            </table>
          </header>
        </div>
      );
    }
}

export default App;
