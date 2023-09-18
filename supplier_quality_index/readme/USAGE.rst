* Install the module.
* Navigate to Settings > SQI > SQI Profile.
* Create a new profile.
* Assign the profile to suppliers.
* Execute the Cron Job titled "Update Supplier Quality Index."

Profile Pyhon Code Sample
~~~~~~~~~~~~~~~~~~~~~~~~~

For this sample, the following modules are necessary:

* Purchase Work Acceptance (OCA)
* Purchase Work Acceptance Evaluation (OCA)

.. code-block:: python

    domain = [
        ('partner_id', '=', record)
    ]

    avg_score = 0
    was = env['work.acceptance'].search(domain)
    score = []

    if was:
        for wa in was:
            for result in wa.evaluation_result_ids:
                score.append(result.score_id.score)
            total_score = sum(score)
        avg_score = total_score/len(was)

    result = avg_score
