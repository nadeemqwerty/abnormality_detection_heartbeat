import React from 'react';
import Artifact from './predictedLabelsMessage/artifact'
import Extrasystole from './predictedLabelsMessage/extrasystole'
import Extrahls from './predictedLabelsMessage/extrahls'
import Murmur from './predictedLabelsMessage/murmur'
import Normal from './predictedLabelsMessage/normal'

const msgStyle = {
    main: {
        borderRadius: 20,
        borderSize: 4,
        borderColor: '#694',
        borderStyle: 'solid'
    },
    header: {
        fontFamily: 'serif',
        background: 'rgb(147, 199, 121)',
        color: 'black',
        fontSize: 40,
        borderRadius: 20,
        borderBottomRightRadius: 0,
        borderBottomLeftRadius: 0
    },
    body: {
        fontFamily: 'serif',
        color: 'black',
        background: 'white',
        borderRadius: 20,
        borderTopRightRadius: 0,
        borderTopLeftRadius: 0
    }
}

function ShowResultMessage(props) {
    const label = props.label;
    let msg = null;
    switch(label) {
        case 'artifact': msg = <Artifact style={msgStyle} val={props.val} />;
                            break
        case 'extrasystole': msg = <Extrasystole style={msgStyle} val={props.val} />
                            break
        case 'extrahls': msg = <Extrahls style={msgStyle} val={props.val} />
                            break
        case 'murmur': msg = <Murmur style={msgStyle} val={props.val} />
                            break
        default: msg = <Normal style={msgStyle} val={props.val} />
                            break
    }
    return msg
}

export default ShowResultMessage;