<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\LetterController;

Route::get('/', function () {
    return view('form');
});

Route::post('/generate-letter', [LetterController::class, 'generate'])->name('generate.letter');

