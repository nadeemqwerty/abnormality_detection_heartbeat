import React from 'react';

function Extrahls(props) {
    return (
        <div style={props.style.main}>
            <header style={props.style.header}>
                Extrahls
            </header>
            <body style={props.style.body}>
                <b>You belong to Extrahls class with a probability score of :-- {props.val}</b>
                <br/>
                In the Artifact category there are a wide range of different sounds, including feedback squeals and echoes, speech, music and noise. There are usually no discernable heart sounds, and thus little or no temporal periodicity at frequencies below 195 Hz. This category is the most different from the others. It is important to be able to distinguish this category from the other three categories, so that someone gathering the data can be instructed to try again.(source: Rita Getz)
            </body>
        </div>
    )
}

export default Extrahls;