import React from 'react';
//import axios from 'axios';

/*
curl -X PUT -d 'isPlaying=false' -d 'currentLink=https://www.youtube.com/watch?v=3iM_06QeZi8' -d 'playList=내 손을 잡아|https://www.youtube.com/watch?v=3iM_06QeZi8|잠 못 드는 밤 비는 내리고|https://www.youtube.com/watch?v=m7mvpe1fVa4' http://127.0.0.1:8000/youtube-remote-player/1/
*/

function PlayList(probs) {
  const playList = probs.playList;
  const listItem = playList.map((item) => 
    <li key = {item.link} > {item.name} </li>
  );

  return <ul>{listItem}</ul>;
}

class App extends React.Component {
  state = {
    isLoading: true,
    isPlaying: false,
    currentLink: "https://www.youtube.com/watch?v=3iM_06QeZi8",    
    playList: []    
  };
/*
  getPlayerInfo = async() => {
    const playerInfo = await axios.get("http://172.30.1.48:8000/youtube-remote-player/1/")
    this.setState({ playerInfo, isLoading: false });
    console.log(playerInfo.data)
  }
*/
  componentDidMount() {
    //this.getPlayerInfo();

    const playerInfo = {
      data :{
        isPlaying: false,
        currentLink: "https://www.youtube.com/watch?v=3iM_06QeZi8",
        playList: "내 손을 잡아|https://www.youtube.com/watch?v=3iM_06QeZi8|잠 못 드는 밤 비는 내리고|https://www.youtube.com/watch?v=m7mvpe1fVa4"
      }
    };

    const parseList = playerInfo.data.playList.split("|");
    let playList = [];    

    for (let i = 0;i < parseList.length;i+=2) {
      playList.push({
        name: parseList[i], 
        link: parseList[i + 1]
      });
    }

    this.setState({      
      isLoading: false,
      isPlaying: playerInfo.data.isPlaying,
      currentLink: playerInfo.data.currentLink,
      playList: playList
    });
  }

  render() {
    const { isLoading, playList } = this.state;

    return (
      <div>
        { 
          isLoading ? "Loading..." :
          <div>             
            <PlayList playList={playList} />
          </div>
        } 
      </div>
    );
  }
}

export default App;
