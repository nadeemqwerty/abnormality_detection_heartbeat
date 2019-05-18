var exec = require('child_process').exec;
var express = require('express');
var app = express();
var multer = require('multer')
var cors = require('cors');

const fname = Date.now() + ""

const PORT = 8000

const COMMAND = "ffmpeg -i public/data/" + fname + " -ac 1 public/data/" + fname + ".wav && python3 backend/backend.py public/data/" + fname + ".wav"

app.use(cors())

var storage = multer.diskStorage({
    destination: function (req, file, cb) {
    cb(null, 'public/data')
  },
  filename: function (req, file, cb) {
    cb(null, fname)
  }
})

var upload = multer({ storage: storage }).single('file')

app.post('/upload',function(req, res) {
    upload(req, res, async function (err) {
            if (err instanceof multer.MulterError) {
                return res.status(500).json(err)
            } else if (err) {
                return res.status(500).json(err)
            }
        let response = (await runPythonScript()).split(',')
        let value = response[0]
        let label = response[1]
        return res.status(200).send({value: value, label: label})
    })
});

app.listen(PORT, function() {
    console.log('App running on port ' + PORT);
});

async function sh(cmd) {
    return new Promise(function (resolve, reject) {
        exec(cmd, (err, stdout, stderr) => {
            if (err) {
                reject(err);
            } else {
                resolve({ stdout, stderr });
            }
        });
    });
}

async function runPythonScript() {
    let { stdout } = await sh(COMMAND);
    return (`${stdout.split('\n')}`);
}
