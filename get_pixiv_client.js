var req = require( 'request' );

// getLogin( pixivId, pixivPass, callback );
// callback( error, client );
// client.get('http://www.pixiv.net/hogehoge', fun(err, res, body) {});
module.exports = function ( id, pass, callback ) {
    var options = {
        url: 'https://www.secure.pixiv.net/login.php',
        form: {
            mode: 'login',
            pixiv_id: id,
            pass: pass
        }
    }

    var client = req.defaults( { jar: true } );
    client.post( options, function ( err, res, body ) {
        return callback( err, client );
    } );
}
