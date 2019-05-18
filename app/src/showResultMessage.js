import React from 'react';
import Artifact from './predictedLabelsMessage/artifact'
import Extrastole from './predictedLabelsMessage/extrastole'
import Extrahls from './predictedLabelsMessage/extrahls'
import Murmur from './predictedLabelsMessage/murmur'
import Normal from './predictedLabelsMessage/normal'

const msgStyle = {
    background: 'blue',
    borderRadius: 20
}

function ShowResultMessage(props) {
    const label = props.label;
    let msg = null;
    switch(label) {
        case 'artifact': msg = <Artifact/>;
                            break
        case 'extrastole': msg = <Extrastole/>
                            break
        case 'extrahls': msg = <Extrahls/>
                            break
        case 'murmur': msg = <Murmur/>
                            break
        default: msg = <Normal/>
                            break
    }
    return (
        <div style={msgStyle}>
            {msg}
        </div>
    )
}

export default ShowResultMessage;