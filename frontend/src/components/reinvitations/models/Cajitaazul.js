import React, {useState} from 'react';
import Buttons from './Buttons';

export default function Cajitaazul(props){
    
    return(
        <div className="cajitachat">
            <div className="textoCajita">
                <div className="row subCajitaAzul">
                    <div className="row">{props.data.msg}</div>
                    {props.data.type === 'invitation' &&
                        <Buttons enviar={props.enviar} setResponse={props.setResponse}/>
                    }
                </div>
            </div>
            <div className="avatarAzul">
                <h1>{props.data.name.toUpperCase()[0]}</h1>
            </div>
        </div>
    )
}
