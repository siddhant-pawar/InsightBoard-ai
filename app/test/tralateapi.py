import requests
import re

# --- Optional: Transcript Sanitization ---
def sanitize_transcript(text: str) -> str:
    """
    Clean and normalize the transcript text:
    - Remove markdown symbols (** __ ## etc.)
    - Normalize whitespace and blank lines
    """
    if not text:
        return ""

    # Replace Markdown special characters
    text = re.sub(r"[\\*_#>`~\-]+", "", text)

    # Replace multiple spaces or tabs with single space
    text = re.sub(r"['' ' \t]+", " ", text)

    # Replace multiple blank lines with a single blank line
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Strip leading/trailing whitespace
    return text.strip()


# --- Raw Transcript ---
raw_transcript = """
Meeting Title: Project Nova - Pre-Launch Engineering & GTM Alignment

Date: February 14, 2024
Attendees: Arjun (Product Manager), Elena (Tech Lead), Carlos (Marketing Director), Zoe (QA Manager)

Arjun: Thanks for joining, everyone. We’re officially two weeks out from Nova’s public beta, so this is our final alignment meeting before launch week. I want to surface any critical blockers and make sure Engineering, QA, and Marketing are fully synced. Elena, can you kick us off with the engineering update?

Elena: Sure, Arjun. We’ve made solid progress. The real-time collaboration feature is now live on staging. But we’ve hit a serious P1 issue — the document sync engine is throwing state conflicts when three or more users edit the same file within a short time window. It doesn’t always cause data loss, but it corrupts the edit history. Obviously, that’s unacceptable for launch.

Arjun: That’s a deal-breaker. What's the root cause?

Elena: We suspect it's the operational transform algorithm not properly resolving overlapping changes from multiple client sessions. I'm refactoring the conflict resolution logic now. Best-case scenario, I can ship a patch by Friday. After that, I’ll need full QA coverage before we lock anything down.

Zoe: We’ll prioritize that, but there’s a catch. Our mobile automation suite hasn’t been running properly on the new iOS 17 simulators — we’re getting random rendering failures in the editor view. So even if we get the patch, testing will take longer than usual unless we can stabilize the environment.

Arjun: Elena, is the mobile rendering issue connected to the sync bug?

Elena: No, completely separate. I think it’s a compatibility issue with the custom font rendering on iOS. It’s minor in the grand scheme, but I can’t promise a fix until after launch. Right now, the real-time sync is the mountain we need to climb.

Arjun: Understood. Zoe, can you commit to manual validation for the sync workflows on both desktop and mobile?

Zoe: Yes, but I’ll need a freeze by Sunday night at the latest. Manual tests on five device types will take my team two full days.

Elena: Copy that. I’ll aim to get you a clean build by Saturday EOD.

Arjun: Great. Carlos, what’s happening on the GTM front?

Carlos: We’re 90% ready. Launch email sequences are written, and the demo video is in post-production. But I need Elena to sign off on the messaging for the real-time editing — particularly around how we describe the conflict resolution. I’d like that feedback by Thursday so I can get final creative approval.

Elena: No problem. Send it my way. I’ll review it after I push the patch.

Carlos: Appreciate it. One more thing — the press deck needs updated screenshots of the collaboration UI with active users editing the same doc. With the current instability, I haven’t been able to capture usable shots.

Arjun: Can we prioritize this once the patch is in and staging is stable?

Elena: Yes, I’ll coordinate with Carlos early next week. Let’s aim for Tuesday.

Carlos: That works. Also, not urgent, but I’d love to A/B test our onboarding sequence post-launch. I think there's room to improve activation in the first 10 minutes.

Arjun: I like that. Can you put together a short brief with test variants and KPIs? We’ll queue it up for post-launch experimentation.

Carlos: Will do.

Zoe: One last thing on my side. Our legacy product, Orion, still has that authentication timeout issue in the admin portal. Support is fielding multiple tickets per week. It's not critical, but it’s not a good look.

Arjun: Yeah, we can’t ignore our existing customers. Elena, any chance you can carve out a few hours to at least diagnose it?

Elena: I can give it three hours next Wednesday. I won’t be able to fully fix it before Nova ships, but I’ll log everything and propose a path forward.

Arjun: That’s all I can ask. Thank you. Alright, to summarize:

The sync engine bug is the top priority.

Stable build by Saturday, full QA starting Sunday.

Elena to review marketing copy by Thursday.

Press screenshots by Tuesday.

Post-launch: onboarding A/B test and Orion auth investigation.

Let’s stay tight on comms this week. Thanks, everyone. Let’s make this happen.
"""

# --- Prepare Cleaned Data Payload ---
sanitized_transcript = sanitize_transcript(raw_transcript)

data = {
    "transcript": sanitized_transcript
}

# --- Send POST Request ---
try:
    response = requests.post("http://localhost:8000/api/transcripts/", json=data)
    print("Status code:", response.status_code)

    # Try to parse JSON if possible
    try:
        print("Response JSON:")
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response is not JSON. Raw response:")
        print(response.text)

except requests.exceptions.RequestException as e:
    print("Request failed:", str(e))
