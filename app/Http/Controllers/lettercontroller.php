<?php
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;

class LetterController extends Controller
{
    public function generate(Request $request)
    {
        $data = $request->validate([
            'name' => 'required|string',
            'to' => 'required|string',
            'reason' => 'required|string',
            'from_date' => 'required|date',
            'to_date' => 'required|date',
        ]);

        $response = Http::post('http://127.0.0.1:5000/generate', $data);

        return view('output', [
            'letter' => $response->json('letter')
        ]);
    }
}

