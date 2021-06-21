import React from 'react';
import axios from 'axios';

/*
curl -X PUT -d 'isPlaying=false' -d 'currentLink=https://www.youtube.com/watch?v=3iM_06QeZi8' -d 'playList=내 손을 잡아|https://www.youtube.com/watch?v=3iM_06QeZi8|잠 못 드는 밤 비는 내리고|https://www.youtube.com/watch?v=m7mvpe1fVa4' http://127.0.0.1:8000/youtube-remote-player/1/
*/

class App extends React.Component {
  state = {
    isLoading: true,
    playerInfo: []
  };

  getPlayerInfo = async() => {
    const playerInfo = await axios.get("http://172.30.1.48:8000/youtube-remote-player/1/")
    this.setState({ playerInfo, isLoading: false });
    console.log(playerInfo.data)
  }

  componentDidMount() {
    this.getPlayerInfo();
  }

  render() {
    const { isLoading, playerInfo } = this.state;
    return (
      <div>
        { 
          isLoading ? "Loading..." :
          <div>
          <p> { playerInfo.data.isPlaying } </p>
          <p> { playerInfo.data.currentLink } </p>
          <p> { playerInfo.data.playList } </p>
          </div>
        } 
      </div>
    );
  }
}

export default App;
