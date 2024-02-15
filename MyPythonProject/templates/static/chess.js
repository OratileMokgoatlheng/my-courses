$(document).ready(function() {
    // Create the chessboard
    for (let i = 0; i < 64; i++) {
        $('#board').append('<div class="square"></div>');
    }

    // Add pieces to the board
    const pieces = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'];
    for (let i = 0; i < 8; i++) {
        $('.square:eq(' + i + ')').text(pieces[i]);
        $('.square:eq(' + (i + 8) + ')').text('P');
        $('.square:eq(' + (i + 48) + ')').text('p');
        $('.square:eq(' + (56 + i) + ')').text(pieces[i].toLowerCase());
    }
});
