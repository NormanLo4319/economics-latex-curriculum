# Hosting the Web-Books on Public GitHub Pages

This repository (`economics-latex-curriculum`) stays **private** so that quiz question banks (`micro/quizzes/`, `macro/quizzes/`), LaTeX source drafts, and internal course documents are never exposed.

When changes are pushed to `web_books/` on `main` (or when you manually trigger the workflow), `.github/workflows/deploy-books.yml` renders both Quarto web-books directly from `web_books/` and publishes **only** the static HTML/CSS/SVG output to a separate **public** GitHub repository.

---

## One-Time GitHub Setup (~5 Minutes)

### 1. Create the Public Publishing Repository
1. On GitHub, create a new **Public** repository named **`economics-web-book`** under `NormanLo4319` (do **not** initialize with a README, `.gitignore`, or license).
   - If you choose a different repository name (for example `NormanLo4319/econ-books`), add a repository variable in `economics-latex-curriculum`: **Settings → Secrets and variables → Actions → Variables → New repository variable** named `PUBLIC_PAGES_REPO` with value `NormanLo4319/<your-repo-name>`.

### 2. Generate an SSH Deploy Key Pair
Run this once in PowerShell (outside the repo, e.g., in `$HOME\.ssh` or a temporary folder):

```powershell
ssh-keygen -t ed25519 -C "github-pages-deploy" -f "$env:USERPROFILE\.ssh\econ_webbooks_deploy" -N '""'
```

This creates two files:
- **Public key:** `%USERPROFILE%\.ssh\econ_webbooks_deploy.pub`
- **Private key:** `%USERPROFILE%\.ssh\econ_webbooks_deploy`

### 3. Add the Public Key to the Public Repo (`economics-web-book`)
1. Open **`NormanLo4319/economics-web-book` → Settings → Deploy keys → Add deploy key**.
2. **Title:** `GitHub Actions Deploy`
3. **Key:** Paste the contents of `econ_webbooks_deploy.pub`.
4. Check **Allow write access** and click **Add key**.

### 4. Add the Private Key to This Private Repo (`economics-latex-curriculum`)
1. Open **`NormanLo4319/economics-latex-curriculum` → Settings → Secrets and variables → Actions → Secrets → New repository secret**.
2. **Name:** `PAGES_DEPLOY_KEY`
3. **Secret:** Paste the full contents of `econ_webbooks_deploy` (including the `-----BEGIN OPENSSH PRIVATE KEY-----` and `-----END OPENSSH PRIVATE KEY-----` lines).
4. Click **Add secret**.

### 5. Push & Trigger the First Deploy
1. Commit and push these changes to `main` on `economics-latex-curriculum`.
2. Open the **Actions** tab on `economics-latex-curriculum` and watch **Deploy E-Textbooks to Public GitHub Pages** complete (~1 minute).
   - You can also run it anytime manually via **Actions → Deploy E-Textbooks to Public GitHub Pages → Run workflow**.

### 6. Enable GitHub Pages on the Public Repo
1. Open **`NormanLo4319/economics-web-book` → Settings → Pages**.
2. Under **Build and deployment**:
   - **Source:** `Deploy from a branch`
   - **Branch:** `main` and folder `/ (root)`
3. Click **Save**.

Within 1–2 minutes, the public site will be live at:
- **Home:** `https://normanlo4319.github.io/economics-web-book/`
- **Microeconomics:** `https://normanlo4319.github.io/economics-web-book/micro/`
- **Macroeconomics:** `https://normanlo4319.github.io/economics-web-book/macro/`

---

## Ongoing Authoring Workflow

1. Edit canonical `.tex` chapters in `micro/chapters/` or `macro/chapters/`.
2. Sync updated `.tex` chapters to Quarto `.qmd` + `.svg` locally:
   ```powershell
   python convert_to_quarto.py --chapter micro/ch03_supply_demand
   ```
   (Or run `python convert_to_quarto.py` to convert all chapters.)
3. (Optional) Preview locally:
   ```powershell
   quarto preview web_books/microeconomics
   ```
4. Commit and push changes under `web_books/` to `main`. GitHub Actions will automatically rebuild and republish the public site.
