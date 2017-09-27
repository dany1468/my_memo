'use strict';

import awsmobile from './aws-exports';
import AWS from 'aws-sdk';

//Filestream setup
var fs = require('fs');
var writeStream =  fs.createWriteStream('mobilehub.html');

var s3 = new AWS.S3();
var s3params = ({
    Bucket: awsmobile.aws_content_delivery_bucket,
    Key: 'index.html'
});

var res = s3.getObject(s3params, function(err, res){
     if (err){
          console.error(err);
     }else {
          writeStream.write(res.Body);
     }
});
