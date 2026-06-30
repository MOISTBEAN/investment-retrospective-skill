import { copyFile, mkdir } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

import { chromium } from "playwright";

const scriptDirectory = path.dirname(fileURLToPath(import.meta.url));
const repositoryRoot = path.resolve(scriptDirectory, "..");
const sourcePath = path.join(
  repositoryRoot,
  "assets",
  "src",
  "social-preview.html",
);
const outputPath = path.join(repositoryRoot, "assets", "social-preview.png");
const docsOutputPath = path.join(
  repositoryRoot,
  "docs",
  "assets",
  "social-preview.png",
);

await mkdir(path.dirname(outputPath), { recursive: true });
await mkdir(path.dirname(docsOutputPath), { recursive: true });

const browser = await chromium.launch({ headless: true });

try {
  const page = await browser.newPage({
    viewport: { width: 1280, height: 640 },
    deviceScaleFactor: 1,
  });

  await page.goto(pathToFileURL(sourcePath).href, { waitUntil: "load" });
  await page.evaluate(() => document.fonts.ready);

  const canvas = await page.evaluate(() => ({
    width: document.documentElement.scrollWidth,
    height: document.documentElement.scrollHeight,
  }));

  if (canvas.width !== 1280 || canvas.height !== 640) {
    throw new Error(
      `Unexpected canvas size: ${canvas.width}x${canvas.height}; expected 1280x640`,
    );
  }

  await page.screenshot({
    path: outputPath,
    type: "png",
    fullPage: false,
    animations: "disabled",
  });
  await copyFile(outputPath, docsOutputPath);

  console.log(
    `Rendered ${path.relative(repositoryRoot, outputPath)} and synced ${path.relative(repositoryRoot, docsOutputPath)} (1280x640)`,
  );
} finally {
  await browser.close();
}
