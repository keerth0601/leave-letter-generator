
<html>
<head>
    <title>Leave Letter Generator</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
<div class="container mt-5">
    <div class="card shadow p-4">
        <h2 class="mb-4">Generate Leave Letter</h2>
        <form method="POST" action="{{ route('generate.letter') }}">
            @csrf
            <div class="mb-3">
                <label class="form-label">Your Name</label>
                <input type="text" name="name" class="form-control" required>
            </div>
            <div class="mb-3">
                <label class="form-label">To (Recipient)</label>
                <input type="text" name="to" class="form-control" required>
            </div>
            <div class="mb-3">
                <label class="form-label">Reason</label>
                <input type="text" name="reason" class="form-control" required>
            </div>
            <div class="mb-3">
                <label class="form-label">From Date</label>
                <input type="date" name="from_date" class="form-control" required>
            </div>
            <div class="mb-3">
                <label class="form-label">To Date</label>
                <input type="date" name="to_date" class="form-control" required>
            </div>
            <button type="submit" class="btn btn-primary">Generate Letter</button>
        </form>
    </div>
</div>
</body>
</html>