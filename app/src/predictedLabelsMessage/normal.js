import React from 'react';

function Normal(props) {
    return (
        <div style={props.style.main}>
            <header style={props.style.header}>
                Normal
            </header>
            <body style={props.style.body}>
                <b>You belong to Normal class with a probability score of :-- {props.val}</b>
                <br/>
                In the Normal category there are normal, healthy heart sounds. These may contain noise in the final second of the recording as the device is removed from the body. They may contain a variety of background noises (from traffic to radios). They may also contain occasional random noise corresponding to breathing, or brushing the microphone against clothing or skin. A normal heart sound has a clear “lub dub, lub dub” pattern, with the time from “lub” to “dub” shorter than the time from “dub” to the next “lub” (when the heart rate is less than 140 beats per minute)(source: Rita Getz)
            </body>
        </div>
    )
}

export default Normal;